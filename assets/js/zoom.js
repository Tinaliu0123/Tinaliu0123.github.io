// Initialize medium zoom.
$(document).ready(function () {
  medium_zoom = mediumZoom("[data-zoomable]", {
    background: getComputedStyle(document.documentElement).getPropertyValue("--global-bg-color") + "ee", // + 'ee' for trasparency.
    // Keep a margin from viewport edges so the zoomed image does not feel flush against the screen.
    margin: 24,
  });
});
