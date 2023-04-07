<template>
  <footer>
    Developed by Vincent Simard-Schmidt
    <br />
    <i>2023</i>
  </footer>
</template>

<script scoped>
export default {
  name: "FooterBar",
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

footer {
  background: var(--main-color-5);
  padding: 4em;
}
</style>
