(() => {
  const root = document.documentElement;
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  const key = "vivek-portfolio-theme";
  let saved = null;
  try { saved = localStorage.getItem(key); } catch { /* Storage is optional. */ }
  if (saved !== "dark" && saved !== "light") saved = null;

  function apply(theme) {
    root.dataset.theme = theme;
    const button = document.querySelector(".theme-toggle");
    if (button) {
      const label = `Switch to ${theme === "dark" ? "light" : "dark"} mode`;
      button.setAttribute("aria-label", label);
      button.title = label;
    }
  }

  apply(saved || (system.matches ? "dark" : "light"));
  function initializeToggle() {
    const button = document.querySelector(".theme-toggle");
    if (!button) return;
    button.hidden = false;
    apply(root.dataset.theme);
    button.addEventListener("click", () => {
      saved = root.dataset.theme === "dark" ? "light" : "dark";
      apply(saved);
      try { localStorage.setItem(key, saved); } catch { /* Still works without persistence. */ }
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeToggle, { once: true });
  } else {
    initializeToggle();
  }
  system.addEventListener("change", () => {
    if (!saved) apply(system.matches ? "dark" : "light");
  });
})();
