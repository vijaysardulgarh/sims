import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/libraries/';

export const getLibraries = () =>
    api.get(endpoint);

export const getLibrary = (id) =>
    api.get(`${endpoint}${id}/`);

export const createLibrary = (
    data
) =>
    api.post(endpoint, data);

export const updateLibrary = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteLibrary = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );