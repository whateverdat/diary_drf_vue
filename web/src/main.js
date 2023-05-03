import { createApp } from 'vue';
import './style.css';
import App from './App.vue';

import Entry from './components/Entry.vue';
import NewEntry from './components/NewEntry.vue';
import Search from './components/Search.vue';

const app = createApp(App);

app.component('Entry', Entry);
app.component('NewEntry', NewEntry);
app.component('Search', Search);

const mountedApp = app.mount('#app');
