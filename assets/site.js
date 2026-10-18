// Theme toggle, list filters, copy-email. The site works without this file.
(function () {
  var root = document.documentElement;

  var tb = document.querySelector(".theme");
  if (tb) tb.addEventListener("click", function () {
    var dark = root.dataset.theme
      ? root.dataset.theme === "dark"
      : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (e) {}
  });

  document.querySelectorAll(".chips").forEach(function (group) {
    var list = group.closest("section").querySelector("[data-list]");
    if (!list) return;
    group.addEventListener("click", function (e) {
      var b = e.target.closest(".chip");
      if (!b) return;
      group.querySelectorAll(".chip").forEach(function (c) {
        c.classList.toggle("on", c === b);
        c.setAttribute("aria-pressed", c === b);
      });
      var f = b.dataset.f;
      Array.prototype.forEach.call(list.children, function (el) {
        var k = el.dataset.kind || el.dataset.cat;
        el.classList.toggle("hide", f !== "all" && k !== f);
      });
    });
  });

  document.querySelectorAll(".copy").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.dataset.copy, old = b.textContent;
      var done = function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = old; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(t).then(done, function () { location.href = "mailto:" + t; });
      else location.href = "mailto:" + t;
    });
  });
})();
