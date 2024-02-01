/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  eslint: { 
    ignoreDuringBuilds: true, 
  }, 
  images: {
    domains: ["lh3.googleusercontent.com","i.pinimg.com"],
  },
 
};

module.exports = nextConfig;
