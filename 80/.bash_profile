function mkdircd() { mkdir -p "$@" && eval cd "\"\$$#\""; }
