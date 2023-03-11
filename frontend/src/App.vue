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
@font-face {
  font-family: "Roboto Mono";
  src: url(assets/robotomono.ttf);
}

* {
  margin: 0;
  padding: 0;
  transition: all 0.1s ease-in;
}

html {
  height: 100%;
}

#app {
  height: 100%;

  background: #061329;
  font-family: "Roboto Mono";
}
</style>
