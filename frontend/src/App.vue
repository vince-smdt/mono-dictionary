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
  --background: #061329;
  --background-hover: #0c2146;
  --text: white;
  --border: white;
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
