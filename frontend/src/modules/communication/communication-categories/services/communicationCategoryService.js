import api from '../../../../services/api/axios';

const endpoint =
    '/communications/communication-categories/';

export const getCommunicationCategories = () =>
    api.get(endpoint);

export const getCommunicationCategory = (id) =>
    api.get(`${endpoint}${id}/`);

export const createCommunicationCategory = (
    data
) =>
    api.post(endpoint, data);

export const updateCommunicationCategory = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteCommunicationCategory = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );