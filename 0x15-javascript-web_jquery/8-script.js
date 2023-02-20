$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data)=> {
  const titles = data.results;
  for (var i=0; i < titles.length; i++) {
    $('#list_movies').append('<li>'+titles[i].title+'</li>');
  }   
});
