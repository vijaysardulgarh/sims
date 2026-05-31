import api from '../../../../services/api/axios';

const endpoint =
    '/communications/circulars/';

export const getCirculars = () =>
    api.get(endpoint);

export const getCircular = (id) =>
    api.get(`${endpoint}${id}/`);

export const createCircular = (
    data
) =>
    api.post(endpoint, data);

export const updateCircular = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteCircular = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );