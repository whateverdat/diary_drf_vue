<script>
export default {
  data() {
    return {
      searchQuery: null,
      field: 'title' || 'content' || 'date',
    };
  },
  watch: {
    field: function () {
      this.searchQuery = null;
    },
  },
};
</script>
<template>
  <!-- Searchbar -->
  <div class="w-full flex flex-col-reverse font-mono">
    <input
      v-model="searchQuery"
      @input="this.$emit('search')"
      class="mx-auto p-2 mt-2 outline-none"
      placeholder="Search..."
      type="text"
    />
    <div class="flex flex-row mx-auto text-sm font-mono mt-4">
      <h1 class="mx-auto">Search within:</h1>
      <input type="radio" id="title" value="title" v-model="field" />
      <label for="title">Title|</label>
      <input type="radio" id="content" value="content" v-model="field" />
      <label for="content">Text|</label>
      <input type="radio" id="date" value="date" v-model="field" />
      <label for="date">Date</label>
    </div>
  </div>
</template>
