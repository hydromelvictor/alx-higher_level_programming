$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(result) {
        $("#character").text(result.name);
});