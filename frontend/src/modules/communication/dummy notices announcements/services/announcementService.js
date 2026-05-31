import api from '../../../../services/api/axios';

const endpoint =
    '/communications/announcements/';

export const getAnnouncements = () =>
    api.get(endpoint);

export const getAnnouncement = (id) =>
    api.get(`${endpoint}${id}/`);

export const createAnnouncement = (
    data
) =>
    api.post(endpoint, data);

export const updateAnnouncement = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteAnnouncement = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );