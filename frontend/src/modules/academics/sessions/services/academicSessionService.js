import api from '../../../../services/api/axios';

const BASE_URL =
    '/academics/sessions/';

export const getAcademicSessions = (
    params = {}
) =>
    api.get(
        BASE_URL,
        { params }
    );

export const getAcademicSession = (
    id
) =>
    api.get(
        `${BASE_URL}${id}/`
    );

export const createAcademicSession = (
    data
) =>
    api.post(
        BASE_URL,
        data
    );

export const updateAcademicSession = (
    id,
    data
) =>
    api.put(
        `${BASE_URL}${id}/`,
        data
    );

export const patchAcademicSession = (
    id,
    data
) =>
    api.patch(
        `${BASE_URL}${id}/`,
        data
    );

export const deleteAcademicSession = (
    id
) =>
    api.delete(
        `${BASE_URL}${id}/`
    );