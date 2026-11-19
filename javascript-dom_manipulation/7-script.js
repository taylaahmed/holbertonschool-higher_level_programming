fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const list = document.querySelector('#list_movies');
    data.results.forEach(function (data) {
      const item = document.createElement('li');
      item.textContent = data.title;
      list.appendChild(item);
    });
  });
