$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (films) {
      $.each(films, function (i, film) {
        $('UL#list_movies').append(film.title);
      });
    }
  });
});
