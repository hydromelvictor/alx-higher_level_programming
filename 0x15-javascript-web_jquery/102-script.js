$('document').ready(()=> {
    $('INPUT#btn_translate').click(()=> {
        const url = 'https://www.fourtonfish.com/hellosalut/hello/';
        $.get(url + $.param({lang: $('INPUT#language_code').val()}), (data)=> {
                $('DIV#hello').html(data.hello);
        });
    });
});