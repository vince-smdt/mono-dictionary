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

:root {
  $main-color: map-get($light-theme, main-color);
  $secondary-color: map-get($light-theme, secondary-color);
  $lcd: map-get($light-theme, lcd);

  --main-color: #{$main-color};
  --secondary-color: #{$secondary-color};

  @for $i from 1 through 10 {
    --main-color-#{$i * 5}: #{scale-color($main-color, $lightness: $i * 5% * $lcd)};
    --secondary-color-#{$i * 5}: #{scale-color($secondary-color, $lightness: $i * 5% * -$lcd)};
  }
}

@media (prefers-color-scheme: dark) {
  :root {
    $main-color: map-get($dark-theme, main-color);
    $secondary-color: map-get($dark-theme, secondary-color);
    $lcd: map-get($dark-theme, lcd);

    --main-color: #{$main-color};
    --secondary-color: #{$secondary-color};

    @for $i from 1 through 10 {
      --main-color-#{$i * 5}: #{scale-color($main-color, $lightness: $i * 5% * $lcd)};
      --secondary-color-#{$i * 5}: #{scale-color($secondary-color, $lightness: $i * 5% * -$lcd)};
    }
  }
}

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
  fill: var(--secondary-color);
}

#app {
  height: 100%;
  background: var(--main-color);
  color: var(--secondary-color);
  font-family: "Roboto Mono";
}

#router-view {
  margin-bottom: 2em;
}
</style>
