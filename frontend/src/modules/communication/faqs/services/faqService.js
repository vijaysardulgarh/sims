import api from "../../../../services/api/axios";

const ENDPOINT = "/communications/faqs/";

export const getFAQs = () =>
    api.get(ENDPOINT);

export const getFAQ = (id) =>
    api.get(`${ENDPOINT}${id}/`);

export const createFAQ = (data) =>
    api.post(ENDPOINT, data);

export const updateFAQ = (id, data) =>
    api.put(`${ENDPOINT}${id}/`, data);

export const deleteFAQ = (id) =>
    api.delete(`${ENDPOINT}${id}/`);