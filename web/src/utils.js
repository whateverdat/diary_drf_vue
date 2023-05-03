import dateFormat, { masks } from 'dateformat';

// Format the date returns from API for the UI
function formatDate(raw) {
  return dateFormat(raw, 'dddd, mmmm dS, yyyy, h:MM:ss TT');
}

export { formatDate };
