import Avatar from "./Avatar";

const AvatarGroup = ({
    users = [],
}) => {
    return (
        <div className="flex -space-x-2">
            {users.map((user) => (
                <Avatar
                    key={user.id}
                    name={user.name}
                    src={user.image}
                />
            ))}
        </div>
    );
};

export default AvatarGroup;