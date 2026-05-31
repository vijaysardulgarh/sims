import api from '../../../../services/api/axios';

const endpoint =
    '/communications/notices/';

export const getNotices = () =>
    api.get(endpoint);

export const getNotice = (id) =>
    api.get(`${endpoint}${id}/`);

export const createNotice = (
    data
) =>
    api.post(endpoint, data);

export const updateNotice = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteNotice = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );