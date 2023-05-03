<script>
import axios from 'axios'; // For communicating with API
import Entry from './components/Entry.vue';
import NewEntry from './components/NewEntry.vue';
import Search from './components/Search.vue';
import { formatDate } from './utils';

export default {
  data() {
    return {
      data: this.initialLoad(), // Consume API to get all Entry data from API
      isNewEntryActive: false, // To store the state of NewEntry component
      index: 0, // Used for pagination
      searchInput: null, // Query entered to the searchbar
      searchField: null, // Selected search option
      searchCounter: 0, // Keep track of how many Entry matches the query
      preLoadText: 'Loading...', // An informative text to be shown to the user
    };
  },
  methods: {
    formatDate,
    // Initial fetch for all the Entries in the database using API
    initialLoad() {
      this.preLoadText = 'Loading...';
      axios
        .get(`http://127.0.0.1:8000/get-all-entries`)
        .then((response) => {
          this.preLoadText = 'Loading...';
          this.data = response.data;
          console.log(this.data);
          this.preLoadText = '';
        })
        .catch((error) => {
          console.log(error);
          this.preLoadText = 'API Error.';
        });
    },
    // Consume API to fetch the updated data from the database
    async load(data) {
      this.preLoadText = 'Loading...';
      // Gives API time to update database
      await new Promise((resolve) => setTimeout(resolve, 100));
      axios
        .get(`http://127.0.0.1:8000/get-all-entries`)
        .then((response) => {
          // To ensure the data is updated properly
          if (response.data.length != data.length) {
            this.data = response.data;
            console.log(this.data);
            this.preLoadText = '';
          } else {
            this.load(data);
          }
        })
        .catch((error) => {
          console.log(error);
          this.preLoadText = 'API Error.';
        });
    },
  },
  components: { Entry, NewEntry, Search },
};
</script>

<template>
  <!-- BEGIN Search  -->
  <!-- Search component will not render if no data loaded in to the client or when there is a preLoadText -->
  <Search
    ref="search"
    @search="
      this.searchInput = this.$refs.search.searchQuery;
      this.searchField = this.$refs.search.field;
    "
  ></Search>
  <!-- When there is input in searchbar, render results matching the query -->
  <div
    v-if="this.searchInput"
    class="flex flex-col justify-center mt-[10vh] p-5 font-mono"
  >
    <template v-if="this.searchField === 'date'" v-for="(entry, index) in data">
      <Entry
        v-if="
          this.formatDate(this.data[index]['date'])
            .toLowerCase()
            .includes(this.searchInput.toLowerCase())
        "
        :entryData="entry"
        @deleted="this.data = this.load(this.data)"
        @vnode-mounted="this.searchCounter++"
        @vnode-unmounted="this.searchCounter--"
      ></Entry>
    </template>
    <template v-else v-for="(entry, index) in data">
      <Entry
        v-if="
          this.data[index][this.searchField]
            .toLowerCase()
            .includes(this.searchInput.toLowerCase())
        "
        :entryData="entry"
        @deleted="this.data = this.load(this.data)"
        @vnode-mounted="this.searchCounter++"
        @vnode-unmounted="this.searchCounter--"
      ></Entry>
    </template>
    <!-- No matching result for the query  -->
    <h1
      class="mx-auto bg-black bg-opacity-5 rounded p-2"
      v-if="this.searchCounter === 0"
    >
      Nothing to show.
    </h1>
  </div>
  <!-- END Search -->
  <!-- BEGIN Main -->
  <div
    v-else-if="!this.preLoadText"
    class="flex flex-col justify-center mt-[10vh] lg:p-5 font-mono"
  >
    <!-- This button controls the NewEntry component -->
    <button
      @click="this.isNewEntryActive = !this.isNewEntryActive"
      v-text="this.isNewEntryActive ? 'Close' : 'New Entry'"
    ></button>
    <NewEntry
      @newEntryCreated="
        this.data = this.load(this.data);
        this.index++;
      "
      v-if="this.isNewEntryActive"
    ></NewEntry>
    <!-- Main view, Entries are rendered based on data -->
    <div v-for="(entry, index) in data">
      <Entry
        v-if="this.index >= index"
        :entryData="entry"
        @deleted="
          this.data = this.load(this.data);
          this.index--;
        "
      ></Entry>
    </div>
    <!-- Increment index to load more Entry -->
    <button
      v-if="this.data && this.index < this.data.length - 1"
      class="mx-auto mt-5"
      @click="this.index++"
    >
      More...
    </button>
  </div>
  <!-- END Main -->
  <!-- Informative text, only rendered while loading or when API failure -->
  <div v-if="this.preLoadText" class="flex h-screen">
    <h1 class="m-auto text-6xl text-white" v-text="this.preLoadText"></h1>
  </div>
  <!-- No matching result for the query  -->
  <div class="w-screen">
    <h1
      class="mx-auto w-fit bg-black bg-opacity-5 rounded p-2"
      v-if="!this.data && !this.preLoadText"
    >
      Nothing to show.
    </h1>
  </div>
</template>
