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
@import "../assets/scss/functions.scss";

footer {
  background: brightness($main-color, 10%);
  padding: 4em;
}
</style>
