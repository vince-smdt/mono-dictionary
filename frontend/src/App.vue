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

<style lang="scss">
@import "./assets/scss/variables.scss";

@font-face {
  font-family: "Roboto Mono";
  src: url(assets/fonts/robotomono.ttf);
}

* {
  margin: 0;
  padding: 0;
}

html {
  height: 100%;
}

svg {
  fill: $secondary-color;
}

#app {
  height: 100%;
  background: $main-color;
  color: $secondary-color;
  font-family: "Roboto Mono";
}

#router-view {
  margin-bottom: 2em;
}
</style>
