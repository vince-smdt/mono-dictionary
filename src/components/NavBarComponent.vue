<template>
  <nav>
    <div @click="$emit('reload')">
      <strong>Mono Dictionary</strong>
    </div>
    <div @click="show_themes = !show_themes" tabindex="0" @blur="show_themes = false">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="18"
        height="18"
        fill="currentColor"
        class="bi bi-circle-half"
        viewBox="0 0 16 16"
      >
        <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
      </svg>
      <DropDownList
        v-if="show_themes"
        id="themes-dropdown"
        :items="themes"
        @item-click="(theme) => $emit('change-theme', theme)"
      />
    </div>
  </nav>
</template>

<script>
import DropDownList from "./DropDownListComponent.vue";

export default {
  name: "NavBar",
  data() {
    return {
      show_themes: false,
    };
  },
  components: {
    DropDownList: DropDownList,
  },
  props: {
    themes: Object,
  },
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

nav {
  background: var(--main-color-10);
  height: $header-height;
  display: flex;
  padding: 0 2em;
  justify-content: space-between;
  align-items: center;
  & > div {
    height: 100%;
    padding: 0 calc($header-height / 2);
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    white-space: nowrap;
    -webkit-user-select: none; /* Safari */
    -moz-user-select: none; /* Firefox */
    -ms-user-select: none; /* IE10+/Edge */
    user-select: none; /* Standard */
    &:hover {
      background: var(--main-color-15);
    }
  }
}

#themes-dropdown {
  position: absolute;
  transform: translate(-50%, calc(50% + calc($header-height / 3)));
}
</style>
