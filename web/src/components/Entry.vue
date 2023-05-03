<script>
import axios from 'axios';
import { formatDate } from '../utils';

export default {
  data() {
    return {
      // Entry info
      date: formatDate(this.entryData.date),
      location: this.entryData.location,
      title: this.entryData.title,
      content: this.entryData.content,
      deleteRequest: false, // Two step check status for deleting Entry
    };
  },
  props: ['entryData'],
  methods: {
    // Consume API to delete Entry
    deleteEntry() {
      axios
        .post('http://127.0.0.1:8000/delete-entry', {
          'entry-id': this.entryData.id,
        })
        .then((response) => {
          this.serverResponse = response['data'];
          console.log(response);
          this.$emit('deleted'); // Letting parent know when to update data
        });
    },
  },
};
</script>

<template>
  <!-- Entry Body -->
  <div
    class="p-5 lg:mx-[5vw] text-white font-mono bg-black bg-opacity-5 rounded-lg mt-1"
  >
    <div>
      <h1 class="text-right text-xs">{{ this.date }} :: {{ this.location }}</h1>
      <h1 class="text-center text-2xl">{{ this.title }}</h1>
      <div
        v-html="this.content"
        class="text-justify lg:mx-[5vw] text-sm mt-5"
      ></div>
      <!-- Delete -->
      <button
        v-if="!this.deleteRequest"
        @click="this.deleteRequest = true"
        class="mt-2 transition-all text-red-700"
      >
        Delete[x]
      </button>
      <form v-else class="flex flex-col transition-all mt-2">
        <h1 class="text-red-700">Are you sure?</h1>
        <button class="mx-0" @click="this.deleteRequest = false">No</button>
        <button class="mx-0 mt-1" @click.prevent="this.deleteEntry()">
          Yes
        </button>
      </form>
      <!-- END Delete -->
    </div>
  </div>
  <!-- END Entry Body -->
</template>
