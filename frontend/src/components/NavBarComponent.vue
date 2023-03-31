<template>
  <nav>
    <span>Simple Dictionary</span>
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-circle-half" viewBox="0 0 16 16">
      <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z"/>
    </svg>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style>
nav {
  background: var(--background-nav);
  height: var(--nav-bar-height);
  display: flex;
  padding: 0 2em;
  justify-content: space-between;
  align-items: center;
}
</style>
