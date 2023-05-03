// fetches and replaces the name of url
$.get('https://swapi.co/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    $('div#character').text(data.name);
  }
});
