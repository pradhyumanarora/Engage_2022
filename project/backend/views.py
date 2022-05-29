from django.shortcuts import render, redirect
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from .util import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# access_token = ""

class AuthURL(APIView):
    def get(self, request, fornat=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)


def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    # global access_token
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')
    post("http://localhost:3000/homepage", data={
        'access_token': access_token,
        'token_type': token_type,
        'refresh_token': refresh_token,
        'expires_in': expires_in,
        'error': error}).json()
    request.session['access_token'] = access_token

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(access_token, token_type, expires_in, refresh_token)

    return redirect('http://localhost:3000/homepage')


# class (APIView):

# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
class IsAuthenticated(APIView):
    def get(self, request, format=None):
        if request.session.get('access_token'):
            return Response({'isAuthenticated': True}, status=status.HTTP_200_OK)
        else:
            return Response({'isAuthenticated': False}, status=status.HTTP_200_OK)
    # try :
    #     if request.session['access_token']:
    #         return Response({'authenticated': True}, status=status.HTTP_200_OK)

    # except:

    #     return Response({'authenticated': False}, status=status.HTTP_200_OK)
        # is_authenticated = is_spotify_authenticated(
        #     self.request.session.session_key)
        # return Response({'status': is_authenticated}, status=status.HTTP_200_OK)


class CurrentSong(APIView):
    def get(self, request, format=None):
        endpoint = "player/currently-playing"
        response = execute_spotify_api_request(request.session['access_token'], endpoint)

        if 'error' in response or 'item' not in response:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        item = response.get('item')
        duration = item.get('duration_ms')
        progress = response.get('progress_ms')
        album_cover = item.get('album').get('images')[0].get('url')
        is_playing = response.get('is_playing')
        song_id = item.get('id')

        artist_string = ""

        for i, artist in enumerate(item.get('artists')):
            if i > 0:
                artist_string += ", "
            name = artist.get('name')
            artist_string += name

        song = {
            'title': item.get('name'),
            'artist': artist_string,
            'duration': duration,
            'time': progress,
            'image_url': album_cover,
            'is_playing': is_playing,
            'votes': 0,
            'id': song_id
        }

        return Response(song, status=status.HTTP_200_OK)
