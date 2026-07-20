import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import toast from "react-hot-toast";

import schoolService from "../services/schoolService";

import { getClusters } from "../../../clusters/services/clusterService";

import SchoolForm from "../components/SchoolForm";

const AddSchoolPage = () => {

    const navigate = useNavigate();

    const [clusters, setClusters] = useState([]);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        loadClusters();

    }, []);

    const loadClusters = async () => {

        try {

            const data = await getClusters();

            console.log("Clusters :", data);

            setClusters(

                data.results ||

                data ||

                []

            );

        }

        catch (error) {

            console.error(error);

            toast.error("Failed to load clusters");

        }

    };

    const handleSubmit = async (formData) => {

        try {

            setLoading(true);

            await schoolService.createSchool(formData);

            toast.success("School created successfully");

            navigate("/dashboard/schools/schools");

        }

        catch (error) {

            console.error(error);

            toast.error("Failed to create school");

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <SchoolForm

            clusters={clusters}

            loading={loading}

            onSubmit={handleSubmit}

        />

    );

};

export default AddSchoolPage;