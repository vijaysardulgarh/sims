const Avatar = ({
    src,
    name = "",
    size = "md",
}) => {

    const sizes = {
        sm: "h-8 w-8",
        md: "h-10 w-10",
        lg: "h-14 w-14",
    };

    if (src) {
        return (
            <img
                src={src}
                alt={name}
                className={`
                    rounded-full
                    object-cover
                    ${sizes[size]}
                `}
            />
        );
    }

    return (
        <div
            className={`
                rounded-full
                bg-blue-600
                text-white
                flex
                items-center
                justify-center
                font-medium
                ${sizes[size]}
            `}
        >
            {name?.charAt(0)}
        </div>
    );
};

export default Avatar;