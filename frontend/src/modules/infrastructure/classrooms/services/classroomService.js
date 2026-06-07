// ============================================
// CLASSROOM SERVICE
// File: classroomService.js
// ============================================

import api from "../../../../services/api/axios";


// ============================================
// GET ALL CLASSROOMS
// ============================================

const getClassrooms = async (
    params = {}
) => {

    const response =
        await api.get(

            "/infrastructure/classrooms/",

            {
                params
            }
        );

    return response.data;
};


// ============================================
// GET SINGLE CLASSROOM
// ============================================

const getClassroom = async (
    id
) => {

    const response =
        await api.get(

            `/infrastructure/classrooms/${id}/`
        );

    return response.data;
};


// ============================================
// CREATE CLASSROOM
// ============================================

const createClassroom = async (
    data
) => {

    const response =
        await api.post(

            "/infrastructure/classrooms/",

            data
        );

    return response.data;
};


// ============================================
// UPDATE CLASSROOM
// ============================================

const updateClassroom = async (

    id,

    data

) => {

    const response =
        await api.put(

            `/infrastructure/classrooms/${id}/`,

            data
        );

    return response.data;
};


// ============================================
// DELETE CLASSROOM
// ============================================

const deleteClassroom = async (
    id
) => {

    const response =
        await api.delete(

            `/infrastructure/classrooms/${id}/`
        );

    return response.data;
};


// ============================================
// EXPORT
// ============================================

const classroomService = {

    getClassrooms,

    getClassroom,

    createClassroom,

    updateClassroom,

    deleteClassroom,
};

export default classroomService;