<template>
  <div id="app" ref="app" :class="current_theme">
    <NavBar :themes="themes" @change-theme="(theme) => change_theme(theme)" />
    <router-view id="router-view" />
    <FooterBar />
  </div>
</template>

<script>
import NavBar from "./components/NavBarComponent.vue";
import FooterBar from "./components/FooterBarComponent.vue";
import themes from "./assets/scss/themes.module.scss";

export default {
  name: "App",
  mounted() {
    // Process theme info
    let processed_themes = {};

    Object.keys(themes).forEach((name) => {
      let theme_info = themes[name].split(", ");

      // Dict with css properties passed to each drop down item to style them
      processed_themes[name] = {
        background: theme_info[0],
        color: theme_info[1],
      };
    });

    this.themes = processed_themes;

    // Load theme from cookies if set
    let cookie_theme = this.$cookies.get("theme");
    if (this.themes[cookie_theme] === undefined) cookie_theme = undefined;
    this.current_theme = cookie_theme ?? this.default_theme;
  },
  data() {
    return {
      themes: {},
      current_theme: "",
      default_theme: "default",
    };
  },
  methods: {
    change_theme(theme) {
      this.$refs.app.classList.value = theme;
      this.$cookies.set("theme", theme, "1y");
    },
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
