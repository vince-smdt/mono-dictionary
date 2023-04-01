<template>
  <div id="app">
    <NavBar />
    <router-view id="router-view" />
    <FooterBar />
  </div>
</template>

<script>
import NavBar from "./components/NavBarComponent.vue";
import FooterBar from "./components/FooterBarComponent.vue";

export default {
  name: "App",
  components: {
    NavBar: NavBar,
    FooterBar: FooterBar,
  },
};
</script>

<style>
:root {
  --nav-bar-height: 3em;
}

:root {
  --text: black;
  --text-hover: #4d4d5b;
  --background: white;
  --background-hover: #e6e6e6;
  --background-light: #eeeeee;
  --background-lighter: #d5d5d5;
  --background-nav: #ededed;
  --background-nav-dropdown: #e2e2e2;
  --background-nav-dropdown-hover: #d4d4d4;
  --background-footer: #ededed;
  --blockquote: #848484;
  --border: black;
}

@media (prefers-color-scheme: dark) {
  :root {
    --text: white;
    --text-hover: #c9c9d6;
    --background: #000000;
    --background-hover: #1d1d1d;
    --background-light: #181818;
    --background-lighter: #222222;
    --background-nav: #282828;
    --background-nav-dropdown: #3d3d3d;
    --background-nav-dropdown-hover: #5f5f5f;
    --background-footer: #0c0c0c;
    --blockquote: #929292;
    --border: white;
  }
}

@font-face {
  font-family: "Roboto Mono";
  src: url(assets/robotomono.ttf);
}

* {
  margin: 0;
  padding: 0;
}

html {
  height: 100%;
}

svg {
  fill: var(--text);
}

#app {
  height: 100%;
  background: var(--background);
  color: var(--text);
  font-family: "Roboto Mono";
}

#router-view {
  margin-bottom: 3em;
}
</style>
