import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/auditoriums/';

export const getAuditoriums = () =>
    api.get(endpoint);

export const getAuditorium = (id) =>
    api.get(`${endpoint}${id}/`);

export const createAuditorium = (
    data
) =>
    api.post(endpoint, data);

export const updateAuditorium = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteAuditorium = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );