<script>
import axios from 'axios';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import CKEditor from '@ckeditor/ckeditor5-vue';

export default {
  data() {
    return {
      form: {
        location: '',
        title: '',
        content: '',
      },
      serverResponse: null,
      // CKEditor settings
      editor: ClassicEditor,
      editorConfig: {
        toolbar: ['Bold', 'Italic', '|', 'Undo', 'Redo'],
      },
    };
  },
  methods: {
    // Consume API to create new Entry
    createNewEntry() {
      axios
        .post('http://127.0.0.1:8000/new-entry', this.form)
        .then((response) => {
          this.serverResponse = response['data'];
          console.log(response);
          this.$emit('newEntryCreated');
        })
        .catch((error) => {
          this.serverResponse = error.response.data;
          console.log(error);
        });
      this.form.location = '';
      this.form.title = '';
      this.form.content = '';
    },
  },
  components: {
    ckeditor: CKEditor.component,
  },
};
</script>
<template>
  <!-- Form -->
  <div>
    <form class="flex flex-col lg:w-1/2 p-2 mx-auto" action="POST">
      <input
        v-model="this.form.location"
        class="mt-2 p-1 outline-none"
        placeholder="Location"
        type="text"
      />
      <input
        v-model="this.form.title"
        class="mt-2 p-1 outline-none"
        placeholder="Title"
        type="text"
      />
      <!-- <textarea
        v-model="this.form.content"
        class="mt-2 p-1 resize-y rounded outline-none"
        placeholder="Content"
        type="text"
      /> -->
      <div class="mt-5">
        <ckeditor
          v-model="this.form.content"
          placeholder="Content"
          :editor="editor"
          :config="editorConfig"
        ></ckeditor>
      </div>
      <!-- Client-side button check -->
      <button
        class="mt-2"
        @click.prevent="this.createNewEntry()"
        :disabled="
          !this.form.location || !this.form.title || !this.form.content
        "
      >
        Done
      </button>
      <!-- Server response -->
      <h2 v-if="this.serverResponse" class="mx-auto text-xs">
        {{ this.serverResponse }}
      </h2>
    </form>
  </div>
</template>
