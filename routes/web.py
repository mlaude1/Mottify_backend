"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    
    RouteGroup([
        Get("/", "TrackController@index").name("index"),
        Get("/@id", "TrackController@show").name("show"),
        Post("/", "TrackController@create").name("create"),
        Put("/@id", "TrackController@update").name("update"),
        Delete("/@id", "TrackController@destroy").name("destroy")
    ], prefix="/track", name="mixtape")
]
