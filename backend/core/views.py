import pathlib
import django.http.response


def graphiql(request):
    """Trivial view to serve the `graphiql.html` file."""
    del request
    graphiql_filepath = pathlib.Path(__file__).absolute().parent / "templates/graphiql.html"
    with open(graphiql_filepath) as f:
        return django.http.response.HttpResponse(f.read())
