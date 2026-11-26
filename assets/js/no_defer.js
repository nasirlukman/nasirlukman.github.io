// Give content tables a clean Bootstrap style.
$(document).ready(function () {
  $("article table").each(function () {
    if ($(this).parents("pre, code").length) return;
    $(this).addClass("table table-sm table-hover");
  });
});
