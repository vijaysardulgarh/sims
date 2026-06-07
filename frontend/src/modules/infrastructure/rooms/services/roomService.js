import api from '../../../../services/api/axios';

const BASE_URL =
    '/infrastructure/rooms/';

// ==========================================
// GET ALL ROOMS
// ==========================================

export const getRooms = (
    params = {}
) =>
    api.get(
        BASE_URL,
        { params }
    );

// ==========================================
// GET SINGLE ROOM
// ==========================================

export const getRoom = (
    id
) =>
    api.get(
        `${BASE_URL}${id}/`
    );

// ==========================================
// CREATE ROOM
// ==========================================

export const createRoom = (
    data
) =>
    api.post(
        BASE_URL,
        data
    );

// ==========================================
// UPDATE ROOM
// ==========================================

export const updateRoom = (
    id,
    data
) =>
    api.put(
        `${BASE_URL}${id}/`,
        data
    );

// ==========================================
// PATCH ROOM
// ==========================================

export const patchRoom = (
    id,
    data
) =>
    api.patch(
        `${BASE_URL}${id}/`,
        data
    );

// ==========================================
// DELETE ROOM
// ==========================================

export const deleteRoom = (
    id
) =>
    api.delete(
        `${BASE_URL}${id}/`
    );