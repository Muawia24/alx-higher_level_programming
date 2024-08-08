$('document').ready(function () {
  function trnaslate () {
    const langCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
    $.get(url, function (data) {
      $('DIV#hello').html(data.hello);
    });
  }
  $('INPUT#btn_translate').click(trnaslate);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});
