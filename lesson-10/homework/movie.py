import requests

API_KEY = "0dde44cb02ed667850275cf6b3d92cd3"

def recommend_movie(movie):
    base_url = "https://developer.themoviedb.org/docs/getting-started/"  
    params = {
        'api_key': API_KEY
    }
    try:

        movie = requests.get(base_url, params=params)
        movie.raise_for_status()
        return {genre["name"].lower():genre["id"] for genre in response.json()["genres"]}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching genres: {e}")
        return None
    
print("movie")

       