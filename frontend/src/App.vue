<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style>

:root {
    --text: black;
    --text-hover: #4d4d5b;
    --background: white;
    --background-light: #eeeeee;
    --background-lighter: #cccccc;
    --background-hover: #e6e6e6;
    --blockquote: #848484;
    --border: black;
  }

@media (prefers-color-scheme: dark) {
  :root {
    --text: white;
    --text-hover: #c9c9d6;
    --background: #061329;
    --background-light: #0c1b36;
    --background-lighter: #132549;
    --background-hover: #0c2146;
    --blockquote: #224c94;
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

#app {
  height: 100%;

  background: var(--background);
  color: var(--text);
  font-family: "Roboto Mono";
}
</style>
