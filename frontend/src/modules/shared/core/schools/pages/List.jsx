import {
    useEffect,
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import CrudHeader from "@/modules/shared/components/crud/CrudHeader";

import DataTable from "@/modules/shared/components/crud/DataTable";

import SearchBox from "@/modules/shared/components/crud/SearchBox";

import schoolService from "../services/schoolService";

const List = () => {

    const navigate = useNavigate();

    const [schools, setSchools] =
        useState([]);

    const [search, setSearch] =
        useState("");

    useEffect(() => {

        fetchSchools();

    }, []);

    const fetchSchools = async () => {

        try {

            const response =
                await schoolService.getSchools();

            const data =

                Array.isArray(response)

                    ? response

                    : response.results || [];

            setSchools(data);

        } catch (error) {

            console.error(error);
        }
    };

    const filteredSchools =
        schools.filter((school) =>

            school.name
                ?.toLowerCase()
                .includes(
                    search.toLowerCase()
                )
        );

    const columns = [

        {
            key: "name",
            label: "Name",
        },

        {
            key: "code",
            label: "Code",
        },

        {
            key: "email",
            label: "Email",
        },
    ];

    return (

        <div className="space-y-6">

            <CrudHeader
                title="Schools"
                addLabel="Add School"
                onAdd={() =>
                    navigate(
                        "/dashboard/core/schools/create"
                    )
                }
            />

            <SearchBox
                placeholder="Search schools..."
                value={search}
                onChange={(e) =>
                    setSearch(e.target.value)
                }
            />

            <DataTable
                columns={columns}
                data={filteredSchools}
            />

        </div>
    );
};

export default List;