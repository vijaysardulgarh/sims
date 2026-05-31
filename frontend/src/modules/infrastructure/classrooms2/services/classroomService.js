import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/classrooms/';

export const getClassrooms = () =>
    api.get(endpoint);

export const getClassroom = (id) =>
    api.get(`${endpoint}${id}/`);

export const createClassroom = (
    data
) =>
    api.post(endpoint, data);

export const updateClassroom = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteClassroom = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );