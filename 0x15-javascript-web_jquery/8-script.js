$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (content) {
  const movies = content.results;
  for (let i = 0; i <= movies.length; i++) {
    $('UL#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
