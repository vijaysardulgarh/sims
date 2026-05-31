import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/playgrounds/';

export const getPlaygrounds = () =>
    api.get(endpoint);

export const getPlayground = (id) =>
    api.get(`${endpoint}${id}/`);

export const createPlayground = (
    data
) =>
    api.post(endpoint, data);

export const updatePlayground = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deletePlayground = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );