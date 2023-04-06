<template>
  <!-- TODO - keep theme even when refreshing page, cookies? -->
  <div id="app" ref="app" class="dark">
    <NavBar :themes="themes" @change-theme="(theme) => change_theme(theme)" />
    <router-view id="router-view" />
    <FooterBar />
  </div>
</template>

<script>
import NavBar from "./components/NavBarComponent.vue";
import FooterBar from "./components/FooterBarComponent.vue";

export default {
  name: "App",
  data() {
    return {
      // TODO - make it so we don't have to define theme names in vue and in scss file, maybe json file with themes in it?
      themes: ["light", "dark", "tropical", "solarized"],
      current_theme: "Light",
    };
  },
  methods: {
    change_theme(theme) {
      this.$refs.app.classList.value = theme;
    }
  },
  components: {
    NavBar: NavBar,
    FooterBar: FooterBar,
  },
};
</script>

<style lang="scss">
@import "./assets/scss/variables.scss";

#app {
  @each $themeName, $theme in $themes {
    .#{$themeName} {
      $main-color: map-get($theme, main-color);
      $secondary-color: map-get($theme, secondary-color);
      $lcd: map-get($theme, lcd);
  
      --main-color: #{$main-color};
      --secondary-color: #{$secondary-color};
  
      @for $i from 1 through 10 {
        --main-color-#{$i * 5}: #{scale-color(
            $main-color,
            $lightness: $i * 5% * $lcd
          )};
        --secondary-color-#{$i * 5}: #{scale-color(
            $secondary-color,
            $lightness: $i * 5% * -$lcd
          )};
      }
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
