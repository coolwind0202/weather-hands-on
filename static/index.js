const elements = ["day-card", "temperature-info", "weather-detail"];

elements.forEach((elmName) => {
  customElements.define(
    elmName,
    class extends HTMLElement {
      constructor() {
        super();
        const template = document.getElementById(elmName).content;

        const shadowRoot = this.attachShadow({ mode: "open" });
        shadowRoot.appendChild(template.cloneNode(true));
      }
    }
  );
});
